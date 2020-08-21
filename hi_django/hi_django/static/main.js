document.querySelector(".copy_url").addEventListener("click", () => {
    let url = document.querySelector("a").innerHTML;       
    navigator.clipboard.writeText(url)        
})
