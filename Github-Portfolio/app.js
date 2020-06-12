fetch("https://api.github.com/users/Junth")
  .then((response) => response.json())
  .then((data) => {
    document.getElementById("name").textContent = data["name"];
    document.getElementById("bio").textContent = data["bio"];
    document.getElementById(
      "followers"
    ).textContent = `Followers: ${data["followers"]}`;
    document.getElementById(
      "following"
    ).textContent = `Following: ${data["following"]}`;
  });

function createRepoList(repoName) {
  var node = document.createElement("LI");
  var textnode = document.createTextNode(repoName);
  node.appendChild(textnode);
  document.getElementById("myList").appendChild(node);
}

fetch("https://api.github.com/users/Junth/repos?page=1&per_page=60")
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    data.map((repo) => {
      console.log(repo.name);
      console.log(repo.created_at.slice(0, 10));
      console.log(repo.description);
      createRepoList(repo.name);
    });
  });
