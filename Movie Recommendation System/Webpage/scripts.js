// Dynamically create and style the webpage
document.addEventListener("DOMContentLoaded", () => {
    // Apply styles via CSS file
    const cssLink = document.createElement("link");
    cssLink.rel = "stylesheet";
    cssLink.href = "stylesss.css";
    document.head.appendChild(cssLink);

    // Create header
    const header = document.createElement("header");
    const headerTitle = document.createElement("h1");
    headerTitle.textContent = "Movie Recommendation System";
    header.appendChild(headerTitle);
    document.body.appendChild(header);

    // Create main section
    const main = document.createElement("main");
    const subtitle = document.createElement("h2");
    subtitle.textContent = "Find Movies Similar to Your Favorites";
    main.appendChild(subtitle);

    const input = document.createElement("input");
    input.type = "text";
    input.placeholder = "Enter a movie name...";
    input.id = "movieInput";
    main.appendChild(input);

    const button = document.createElement("button");
    button.textContent = "Get Recommendations";
    main.appendChild(button);

    const resultsDiv = document.createElement("div");
    resultsDiv.id = "results";
    main.appendChild(resultsDiv);

    document.body.appendChild(main);

    // Button click event
    button.addEventListener("click", () => {
        const movieName = input.value.trim();
        if (!movieName) {
            alert("Please enter a movie name!");
            return;
        }

        fetch(`http://127.0.0.1:5000/recommend?movie=${encodeURIComponent(movieName)}`)
            .then((response) => {
                if (!response.ok) throw new Error("Failed to fetch recommendations");
                return response.json();
            })
            .then((data) => {
                resultsDiv.innerHTML = "<h3>Recommended Movies:</h3>";
                if (data.recommendations && data.recommendations.length > 0) {
                    const list = document.createElement("ul");
                    data.recommendations.forEach((movie) => {
                        const listItem = document.createElement("li");
                        listItem.textContent = movie;
                        list.appendChild(listItem);
                    });
                    resultsDiv.appendChild(list);
                } else {
                    resultsDiv.innerHTML += "<p>No recommendations found.</p>";
                }
            })
            .catch((error) => {
                console.error(error);
                alert("An error occurred while fetching recommendations.");
            });
    });
});
