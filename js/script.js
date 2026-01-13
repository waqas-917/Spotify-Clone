const { createElement } = require("react");

console.log("Script loaded successfully.");


async function get_songs(Folder){
    let current_folder = Folder
    let a = await fetch(`/${Folder}/`) 
    let response = a.text()
    let div = document.createElement("div")
    div.innerHTML = response
    // let as = div.getElementsByTagName("a")
}