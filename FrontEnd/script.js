document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault(); 
    const queryInput = document.querySelector('.tec').value;
    if (queryInput) {
        // Remove initial h1 only if it exists (first submission)
        const wel = document.querySelector('.wel');
        if (wel) {
            if (wel) {
                wel.remove();
        }}

        // Move ProjGen to the top
        const projgen = document.querySelector('.projgen');
        if (projgen ) {
            // Set initial styles for smooth transition
            projgen.style.position = 'absolute';
            projgen.style.left = '45%';
            projgen.style.top = '10%';
            projgen.style.opacity = '0'; // Start hidden
            projgen.style.transform = 'translateY(20px)'; // Start slightly below

            // Trigger the transition
            setTimeout(() => {
                projgen.style.transition = 'transform 1ms linear, opacity 2s ease-in-out';
                projgen.style.opacity = '1'; // Fade in
                projgen.style.transform = 'translateY(0)'; // Move to original position
            }, 10); // Small delay to allow the browser to register the initial styles
        }
        


        // Create new query display
        // 
        // Simulate AI response (frontend only)
        setTimeout(() => {
            // Create response bubble
            const responseDisplay = document.createElement('div');
            responseDisplay.className = 'response-display text-box';

            const responseText = document.createElement('div');
            responseText.className = 'ai-response';
            responseText.style.padding = '10px';
            responseText.style.textAlign = 'left';
            responseText.style.backgroundColor = 'rgba(240, 240, 255, 1)';
            responseText.style.border = '2px solid rgba(200, 200, 255, 1)';
            responseText.style.borderRadius = '20px';
            responseText.style.color = 'rgb(30, 30, 80)';
            responseText.style.pointerEvents = 'none';
            responseText.style.display = 'inline-block';
            responseText.style.whiteSpace = 'normal';
            responseText.style.maxWidth = '400px';
            responseText.style.minWidth = '50px';
            responseText.textContent = 'This is a simulated AI response for: ' + queryInput;

            responseDisplay.style.opacity = '0';
            responseDisplay.style.transform = 'translate(-50%, -40%)';
            responseDisplay.style.transition = 'opacity 0.3s ease-in, transform 0.3s ease-out';
            responseText.style.opacity = '0';
            responseText.style.transition = 'opacity 0.3s ease-in, transform 0.3s ease-out';
            // Fetch AI response from backend
            // Dynamically adjust wrapper height for new responses
            const updateWrapperHeight = () => {
                const allDisplays = document.querySelectorAll('.query-display, .response-display');
                let maxBottom = 0;
                allDisplays.forEach(el => {
                    const rect = el.getBoundingClientRect();
                    maxBottom = Math.max(maxBottom, rect.bottom);
                });
                const wrapperRect = wrapper.getBoundingClientRect();
                if (maxBottom > wrapperRect.bottom) {
                    wrapper.style.height = (maxBottom - wrapperRect.top + 40) + 'px';
                }
            };

            // Fetch AI response from backend
            fetch('AIzaSyBy1WqPeSNlioWpJaYsHJG_YSHjtFKxkEs', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query: queryInput })
            })
            .then(response => response.json())
            .then(data => {
                responseText.textContent = data.response || 'No response from AI.';
                updateWrapperHeight();
            })
            .catch(() => {
                responseText.textContent = 'Error connecting to AI backend.';
                updateWrapperHeight();
            });

            // Also update height after animation
            setTimeout(updateWrapperHeight, 400);
            const chatContainer = document.querySelector('.chat-container');

// Create user bubble
const queryDisplay = document.createElement('div');
queryDisplay.className = 'query-display';
queryDisplay.textContent = queryInput;
chatContainer.appendChild(queryDisplay);
chatContainer.scrollTop = chatContainer.scrollHeight; // auto-scroll

// Simulate / fetch AI response
setTimeout(() => {
    const responseDisplay = document.createElement('div');
    responseDisplay.className = 'response-display';
    responseDisplay.textContent = 'This is a simulated AI response for: ' + queryInput;

    chatContainer.appendChild(responseDisplay);
    chatContainer.scrollTop = chatContainer.scrollHeight; // auto-scroll
}, 700);

            wrapper.appendChild(responseDisplay);

            // Position response below the query
            responseDisplay.style.position = 'absolute';
            responseDisplay.style.left = '80%';
            responseDisplay.style.width = '100%';
            responseDisplay.style.maxWidth = '700px';
            responseDisplay.style.zIndex = '10';
            responseDisplay.style.top = `calc(50% + ${verticalOffset + 40}px)`;

            setTimeout(() => {
            responseDisplay.style.opacity = '1';
            responseDisplay.style.transform = `translate(-50%, -50%)`;
            responseText.style.opacity = '1';
            responseText.style.transform = 'translateY(0)';
            }, 10);
        }, 700); // Simulate delay
        queryText.style.transition = 'opacity 0.3s ease-in, transform 0.3s ease-out';

        queryDisplay.appendChild(queryText);

        const wrapper = document.querySelector('.wrapper');
        wrapper.appendChild(queryDisplay); // Append instead of insertBefore to avoid form overlap

        // Dynamic positioning
        queryDisplay.style.position = 'absolute';
        queryDisplay.style.left = '80%';
        queryDisplay.style.width = '100%';
        queryDisplay.style.maxWidth = '700px';
        queryDisplay.style.zIndex = '10'; // Ensure visibility over other elements

        // Calculate vertical position
        const existingDisplays = document.querySelectorAll('.query-display');
        const index = Array.from(existingDisplays).indexOf(queryDisplay);
        const verticalOffset = index * 70; // Increased to 70px for better spacing
        queryDisplay.style.top = `calc(50% + ${verticalOffset}px)`;

        // Animation
        setTimeout(() => {
            queryDisplay.style.opacity = '1';
            queryDisplay.style.transform = `translate(-50%, -50%)`;
            queryText.style.opacity = '1';
            queryText.style.transform = 'translateY(0)';
        }, 10);

        document.querySelector('.tec').value = ''; // Clear input
    }
});