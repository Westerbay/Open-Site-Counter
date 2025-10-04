class DisplayInformation {

    constructor() {
        this.hostnameInput = $("#hostnameInput");
        this.result = $("#result");
        this.getStatsForm = $("#getStatsForm");
        this.openModal = $("#openModal");
        this.overlayModal = $("#overlay, #modal");
        this.closeModalOverlay = $("#closeModal, #overlay");
    }   

    addEventListeners() {
        this.getStatsForm.on("submit", (e) => {
            e.preventDefault();
            const hostname = this.hostnameInput.val().trim();
            if (!hostname) {
                alert("Hostname missing !");
                return;
            }

            this.result.html("<p>Loading...</p>");
            this.sendRequest(hostname);
        });
        this.openModal.on("click", (e) => {
            e.preventDefault();
            this.overlayModal.removeClass("hidden");
        });
        this.closeModalOverlay.on("click", () => {
            this.overlayModal.addClass("hidden");
        });
    }

    sendRequest(hostname) {
        this.result.removeClass("hidden");
        $.ajax({
            url: "https://wester.games/opensitecounter/get",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ hostname: hostname }),
            success: this.success.bind(this),
            error: this.error.bind(this)
        });
    }

    success(response) {
        if (!response.ok) {
            this.result.html("<p class='error'>Error : " + (response.message || "unknown") + "</p>");
            return;
        }
        const html = `
            <h3>Results for <a href="${response.hostname}">${response.hostname}</a></h3>
            <ul>
                <li>Total connections : <strong>${response.total_occurrences}</strong></li>
                <li>Unique connections : <strong>${response.unique_visitors}</strong></li>
            </ul>
            <img class="graph" src="data:image/png;base64,${response.graph_png_base64}" 
                alt="Connection graph" />
        `;
        this.result.html(html);
    }

    error(xhr) {
        console.error(xhr);
        this.result.html("<p class='error'>Server error.</p>");
    }

}
