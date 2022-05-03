function getQueryVariable(variable) {
    let query = window.location.search.substring(1);
    let vars = query.split("&");
    for (let i=0;i<vars.length;i++) {
        let pair = vars[i].split("=");
        if(pair[0] == variable){return pair[1];}
    }
    return(false);
}


function get(url) {
//const get = (url) => {
    return fetch(url, {mode: 'cors'})
    .then(res => {
        if(res.status === 200) {
            return res.json()
        } else {
            return new Promise.reject(res.json())
        }
    })
    .catch(err => {
        console.log(err)
    })
}

// get("http://localhost:8080/check/1b9bfc7f-7394-4766-ae52-148f89e343ec")


function castrated_text(data) {
    if (data) {
        return "*喵星粗口*"
    } else {
        return "人类你嘎不到我~"
    }
}

function rip_text(data) {
    if (data) {
        return "回喵星啦~"
    } else {
        return "才没有，今天也是元气满满~"
    }
}

function update(data) {
    document.getElementById("name").innerText += data.name
    document.getElementById("sex").innerText += data.sex
    document.getElementById("color").innerText += data.color
    document.getElementById("birth").innerText += data.birth
    document.getElementById("nid").innerText += data.nid
    document.getElementById("relation").innerText += data.relation
    document.getElementById("castrated").innerText += castrated_text(data.castrated)
    document.getElementById("rip").innerText += rip_text(data.rip)
    data.features.forEach(item => {
        createNewNode("#features", item)
    });
    // 后面加的
    data.like.forEach(item => {
        createNewNode("#like", item)
    });
    data.dislike.forEach(item => {
        createNewNode("#dislike", item)
    });
}

/**
 * @function createNewNode
 * @param {String} context 上下文的选择器
 * @param {String} content
 * @description 创建一个新的content作为元素node加入到context中
 */
const createNewNode = (context, content) => {
    context = document.querySelector(context)
    // let newNode = document.createElement("div")
    // newNode.setAttribute("class", "input-group mb-3 form-control")
    // newNode.innerText = content
    // let newContent = document.createTextNode(newNode)
    // context.appendChild(newNode)
    context.innerText += " " + content
}

window.onload = () => {
    // let data = get("http://localhost:8080/check/"+getQueryVariable("nid"))
    //get("http://localhost:9888/check/"+getQueryVariable("nid"))
    get("http://nya-archive-api:9888/check/"+getQueryVariable("nid"))
    .then(res => {
        // console.log(res.data)
        update(res.data)
    })
    // console.log(getQueryVariable("nid"))
}
