document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const queryInput = document.querySelector('.tec').value.trim();

    if (queryInput) {
        // Clear input immediately
        document.querySelector('.tec').value = '';

        // Remove welcome text once
        const wel = document.querySelector('.wel');
        if (wel) wel.remove();

        // Move projgen to top (frontend animation)
        const projgen = document.querySelector('.projgen');
        if (projgen) {
            projgen.style.position = 'absolute';
            projgen.style.left = '45%';
            projgen.style.top = '10%';
            projgen.style.opacity = '0';
            projgen.style.transform = 'translateY(20px)';

            setTimeout(() => {
                projgen.style.transition = 'transform 1ms linear, opacity 2s ease-in-out';
                projgen.style.opacity = '1';
                projgen.style.transform = 'translateY(0)';
            }, 10);
        }

        const chatContainer = document.getElementById('chat-container');

        // === Create User Bubble ===
        const userBubble = document.createElement('div');
        userBubble.className = 'message user-message';
        userBubble.textContent = queryInput;
        chatContainer.appendChild(userBubble);

        chatContainer.scrollTop = chatContainer.scrollHeight;

        // === Send to Backend ===
        fetch("./", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: `query=${encodeURIComponent(queryInput)}`
        })
        .then(response => response.json())
        .then(data => {
            // === Create Bot Bubble ===
            const botBubble = document.createElement('div');
            botBubble.className = 'message bot-message';
            botBubble.innerHTML = marked.parse(data.response || "No response from AI.");

            chatContainer.appendChild(botBubble);

            // Highlight code blocks if any
            botBubble.querySelectorAll("pre code").forEach(block => {
                hljs.highlightElement(block);
            });

            chatContainer.scrollTop = chatContainer.scrollHeight; // auto scroll
        }) 
        .catch(() => {
            const errorBubble = document.createElement('div');
            errorBubble.className = 'message bot-message error';
            errorBubble.textContent = "⚠️ Error connecting to backend.";
            chatContainer.appendChild(errorBubble);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        });
    }
});
