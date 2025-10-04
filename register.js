class Register {

    constructor() {
        this.hostname = window.location.hostname;
    }

    isValid() {
        return this.hostname != "" && this.hostname != "localhost";
    }

    request() {        
        if (!this.isValid()) {
            console.log("Could not register the visit, please verify your hostname");
            return;
        }
        $.ajax({
            url: "https://wester.games/opensitecounter/register",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ hostname: this.hostname }),
            success: this.success,
            error: this.error
        });
    }

    success(response) {
        if (!response.ok) {
            console.log("Could not register the visit, please verify your hostname");
        }
    }

    error(xhr) {
        console.log(xhr);
        console.log("Server error");
    }

}

$(document).ready(function() {
    const register = new Register();
    register.request();
});
