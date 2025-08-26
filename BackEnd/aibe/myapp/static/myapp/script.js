document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const queryInput = document.querySelector('.tec').value.trim();
    if (queryInput) {
        const chatContainer = document.getElementById('chat-container');

        // Show user message
        const userBubble = document.createElement('div');
        userBubble.className = 'message user-message';
        userBubble.textContent = queryInput;
        chatContainer.appendChild(userBubble);

        chatContainer.scrollTop = chatContainer.scrollHeight;

        // Send to backend
        fetch("", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: `query=${encodeURIComponent(queryInput)}`
        })
        .then(response => response.json())
        .then(data => {
            const botBubble = document.createElement('div');
            botBubble.className = 'message bot-message';
            botBubble.innerHTML = marked.parse(data.response);
            chatContainer.appendChild(botBubble);

            // highlight newly added code blocks
            botBubble.querySelectorAll("pre code").forEach(block => {
                hljs.highlightElement(block);
            });

            chatContainer.scrollTop = chatContainer.scrollHeight;
        })
        .catch(err => console.error("Fetch error:", err));

        document.querySelector('.tec').value = '';
    }
});
