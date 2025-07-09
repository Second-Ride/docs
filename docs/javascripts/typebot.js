document$.subscribe(function() {
    console.log("Typebot script loaded");
    
    // Load the Typebot library
    const script = document.createElement("script");
    script.type = "module";
    script.innerHTML = `
        import Typebot from 'https://cdn.jsdelivr.net/npm/@typebot.io/js@0/dist/web.js';
        
        Typebot.initBubble({
            typebot: "faqs",
            apiHost: "https://bot.second-ride.de",
            theme: {
                button: { backgroundColor: "#E4B854" },
                chatWindow: { backgroundColor: "#fff" },
            },
        });
    `;
    document.head.appendChild(script);
});