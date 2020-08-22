document.querySelector(".copy_url").addEventListener("click", () => {
//    let url = document.querySelector(".a").innerHTML;
//    console.log(url);
//    navigator.clipboard.writeText(document.querySelector(".a").innerHTML);
    let ta = document.querySelector(".a");
    let range = document.createRange();
    range.selectNode(ta);
    window.getSelection().addRange(range);

    //пытаемся скопировать текст в буфер обмена
    try {
    document.execCommand('copy');
    } catch(err) {
    console.log('Can`t copy, boss');
    }
    //очистим выделение текста, чтобы пользователь "не парился"
    window.getSelection().removeAllRanges();
});
