class Register {

    constructor() {
        this.hostname = window.location.hostname;
    }

    isValid() {
        return this.hostname != "" && this.hostname != "localhost";
    }

    request(hostname) {        
        if (!this.isValid()) {
            console.log("Could not register the visit, please verify your hostname");
            return;
        }
        fetch("https://wester.games/opensitecounter/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ hostname: hostname })
        })
    }

}

document.addEventListener('DOMContentLoaded', function() {
    const register = new Register();
    register.request(window.location.hostname);
    register.request(window.location.href);
});

