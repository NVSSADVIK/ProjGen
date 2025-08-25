document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault(); 
    const queryInput = document.querySelector('.tec').value;
    if (queryInput) {
        // Remove initial h1 only if it exists (first submission)
        const h1 = document.querySelector('.wrapper h1');
        if (h1) {
            h1.remove();
        }

        // Create new query display
        const queryDisplay = document.createElement('div');
        queryDisplay.className = 'query-display text-box';

        const queryText = document.createElement('div');
        queryText.className = 'tec';
        queryText.style.paddingTop = '10px';
        queryText.style.paddingBottom = '10px';
        queryText.style.paddingLeft = '10px';
        queryText.style.paddingRight = '2.5px';
        queryText.style.textAlign = 'left';
        queryText.style.backgroundColor = 'rgba(255, 255, 255, 0.73)'; 
        queryText.style.border = '2px solid rgba(255, 255, 255, 1)';
        queryText.style.borderRadius = '20px';
        queryText.style.color = 'rgb(0, 0, 0)';
        queryText.style.pointerEvents = 'none'; 
        queryText.style.display = 'inline-block';
        queryText.style.whiteSpace = 'normal';   // allows wrapping
        queryText.style.maxWidth = '400px';      // limit bubble width
        queryText.style.minWidth = '50px';       // small min size

        queryText.textContent = queryInput;
        queryDisplay.style.opacity = '0';
        queryDisplay.style.transform = 'translate(-50%, -40%)';
        queryDisplay.style.transition = 'opacity 0.3s ease-in, transform 0.3s ease-out';
        queryText.style.opacity = '0';
        queryText.style.transform = 'translateY(10px)';
        queryText.style.transition = 'opacity 0.3s ease-in, transform 0.3s ease-out';

        queryDisplay.appendChild(queryText);

        const wrapper = document.querySelector('.wrapper');
        wrapper.appendChild(queryDisplay); // keep as your dev made

        // Dynamic positioning
        const existingDisplays = document.querySelectorAll('.query-display');
        const index = Array.from(existingDisplays).indexOf(queryDisplay);
        const verticalOffset = index * 70; // Increased to 70px for better spacing
        queryDisplay.style.position = 'absolute';
        queryDisplay.style.left = '80%';
        queryDisplay.style.top = `calc(50% + ${verticalOffset}px)`;
        queryDisplay.style.width = '100%';
        queryDisplay.style.maxWidth = '700px';
        queryDisplay.style.zIndex = '10'; // Ensure visibility over other elements

        // Animation
        setTimeout(() => {
            queryDisplay.style.opacity = '1';
            queryDisplay.style.transform = `translate(-50%, -50%)`;
            queryText.style.opacity = '1';
            queryText.style.transform = 'translateY(0)';
        }, 10);

        // ✅ Send query to Django so it prints in terminal
        fetch("/chatbot/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: `query=${encodeURIComponent(queryInput)}`
        });

        document.querySelector('.tec').value = ''; // Clear input
    }
});
