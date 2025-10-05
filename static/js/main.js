document.addEventListener("DOMContentLoaded", function () {
	console.log("DOM fully loaded and parsed");
  const titleInput = document.getElementById("titleInput");
  const suggestionsBox = document.getElementById("suggestions");
  const suggestionsList = suggestionsBox.querySelector("ul");
  const resultsContainer = document.getElementById("results");
  const keywordsContainer = document.getElementById("keywords");

  // Show suggestions as user types
  titleInput.addEventListener("input", () => {
    const value = titleInput.value.toLowerCase().trim();
    suggestionsList.innerHTML = "";
    if (!value) {
      suggestionsBox.style.display = "none";
      return;
    }

    // Fetch suggestions from backend
    fetch("/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: value })
    })
    .then(res => res.json())
    .then(data => {
      const matched = data.keywords || [];
      if (matched.length === 0) {
        suggestionsBox.style.display = "none";
        return;
      }

      matched.forEach(keyword => {
        const li = document.createElement("li");
        li.textContent = keyword;
        li.style.padding = "8px";
        li.style.cursor = "pointer";
        li.addEventListener("click", () => {
          titleInput.value = keyword;
          suggestionsBox.style.display = "none";
          showResults(keyword);
        });
        suggestionsList.appendChild(li);
      });

      suggestionsBox.style.display = "block";
    })
    .catch(err => console.error(err));
  });

  // Hide suggestions when clicking elsewhere
  document.addEventListener("click", e => {
    if (!suggestionsBox.contains(e.target) && e.target !== titleInput) {
      suggestionsBox.style.display = "none";
    }
  });

  // Handle form submit
  const searchForm = document.getElementById("internship-search");
  searchForm.addEventListener("submit", e => {
    e.preventDefault();
    showResults(titleInput.value);
  });

  // Display results and backend keywords
  function showResults(query) {
    resultsContainer.innerHTML = "";
    keywordsContainer.innerHTML = "";
    const value = query.toLowerCase().trim();

    fetch("/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: value })
    })
    .then(res => res.json())
    .then(data => {
      const opportunities = data.opportunities || [];
      const keywords = data.keywords || [];

      // Display related keywords
      if (keywords.length > 0) {
        keywordsContainer.innerHTML = `Related keywords: ${keywords.join(", ")}`;
      }

      // Display internships
      if (opportunities.length === 0) {
        resultsContainer.innerHTML = `<p>No results found for "<strong>${query}</strong>".</p>`;
        return;
      }

      opportunities.forEach(i => {
        const card = document.createElement("div");
        card.classList.add("job-card");
        card.innerHTML = `
          <h3>${i.title}</h3>
          <p><strong>${i.company}</strong></p>
          <p>${i.location}</p>
          <a href="${i.link}" class="apply" target="_blank">Apply Now</a>
        `;
        resultsContainer.appendChild(card);
      });
    })
    .catch(err => console.error(err));
  }
});
