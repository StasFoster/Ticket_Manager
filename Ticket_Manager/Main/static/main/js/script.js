// glow след за курсором
document.querySelectorAll('.task-card').forEach(card => {
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--x', (e.clientX - rect.left) + 'px');
        card.style.setProperty('--y', (e.clientY - rect.top) + 'px');
    });
});
// универсальный hover glow
document.querySelectorAll('.team-card, .task-card').forEach(card => {
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--x', (e.clientX - rect.left) + 'px');
        card.style.setProperty('--y', (e.clientY - rect.top) + 'px');
    });
});

const status_list = document.querySelectorAll(".status-select")

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

async function getListTask(){
    await fetch("/tasks/")
        .then(data=>data.json())
        .then(data=>{
            object_list = data["message"]
            console.log(data);
            console.log(data["message"]);
            
        })
    console.log("asasasaasasas");
}
function CheckStatus(){
    let id = this.dataset.id
    let value = this.value
    const csrftoken = getCookie('csrftoken');
    fetch("/tasks/" + id + "/", {
        method: "PATCH",
        headers:{
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            status:value,
        })
    })
}

status_list.forEach(select => {
    select.addEventListener("change", CheckStatus)
})

document.addEventListener("DOMContentLoaded", ()=>{getListTask()})


