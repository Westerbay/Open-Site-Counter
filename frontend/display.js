class DisplayInformation {

    constructor() {
        this.hostnameInput = $("#hostnameInput");
    }   

    addEventListeners() {
        $("#getStatsForm").on("submit", (e) => {
            e.preventDefault();
            const hostname = this.hostnameInput.val().trim();
            if (!hostname) {
                alert("Hostname missing !");
                return;
            }

            $("#result").html("<p>Loading...</p>");
            this.sendRequest(hostname);
            
        });
    }

    sendRequest(hostname) {
        $.ajax({
            url: "http://127.0.0.1:5001/get",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ hostname: hostname }),
            success: this.success,
            error: this.error
        });
    }

    success(response) {
        if (!response.ok) {
            $("#result").html("<p style='color:red;'>Erreur : " + (response.message || "inconnue") + "</p>");
            return;
        }
        const html = `
            <h3>Résultats pour <em>${response.hostname}</em></h3>
            <ul>
                <li>Total connexions : <strong>${response.total_occurrences}</strong></li>
                <li>Visiteurs uniques : <strong>${response.unique_visitors}</strong></li>
            </ul>
            <img src="data:image/png;base64,${response.graph_png_base64}" 
                alt="Graphique des connexions" 
                style="max-width:100%; border:1px solid #ccc; border-radius:8px; box-shadow:0 0 8px rgba(0,0,0,0.1);" />
        `;
        $("#result").html(html);
    }

    error(xhr) {
        console.error(xhr);
        $("#result").html("<p style='color:red;'>Server error.</p>");
    }

}
