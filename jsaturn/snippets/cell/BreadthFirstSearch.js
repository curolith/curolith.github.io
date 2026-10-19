console.log(`Following the <a href="https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode">Wikipedia pseudocode</a>`)

const adjacencyLists = [
    [1, 2], // Node 0 has edges to 1 and 2
    [3, 4],
    [5, 6],
    [],
    [7],
    [],
    [],
    []
];

const q = [0];
const explored = new Array(adjacencyLists.length);
const parents = new Array(adjacencyLists.length);
parents[0] = "root";
explored[0] = true;
console.log("Explored 0");
while (q.length) { // 0 is falsy
    let v = q.shift(); // Remove first element
    adjacencyLists[v].forEach(w => {
        if (explored[w]) {
            return; // return from forEach
        }
        explored[w] = true;
        console.log("Explored " + w);
        parents[w] = v;
        q.push(w); // Add to end
    })
}

console.log("Explored: " + explored);
console.log("Parents: " + parents);

console.log("Visualization:")
console.log(`<img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled">\n`);
console.log("Credit for the gif:");
console.log(`By Blake Matheny - Transferred from <span class="plainlinks"><a class="external text" data-mw-original-href="//en.wikipedia.org" href="https://en.wikipedia.org">en.wikipedia</a></span> to Commons., <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=1864649">Link</a>`);