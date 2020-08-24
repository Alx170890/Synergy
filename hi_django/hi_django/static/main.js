document.querySelector(".copy_url").addEventListener("click", () => {
    let range = document.createRange();
    range.selectNode(document.querySelector(".a"));
    window.getSelection().addRange(range);
    try {
    document.execCommand('copy');
    } catch(err) {
    console.log('Can`t copy, boss');
    }
    window.getSelection().removeAllRanges();
});
