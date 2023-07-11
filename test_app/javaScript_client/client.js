const loginForm = document.getElementById('login-form');
const searchForm = document.getElementById('search-form');
const contentContainer = document.getElementById('content-container');

const baseEndpoint = 'http://localhost:8000'

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm) {
    searchForm.addEventListener('submit', handleSearch)
}

function handleLogin(event) {
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/api/token/`;
    const formData = new FormData(loginForm);
    const formObjectData = Object.fromEntries(formData);
    const formStrObjectData = JSON.stringify(formObjectData);
    const { username, password } = formObjectData
    const options = {
        "method": "POST",
        "headers": {
            'Content-Type': 'application/json'
        },
        "body": formStrObjectData
    };
    fetch(loginEndpoint, options).then(response => {
        return response.json();
    }).then(authData => {
        handleAuth(authData, getProductList);
    }).catch(err => {
        console.log("err: ", err);
    })
}

function handleSearch(event) {
    event.preventDefault();
    const formData = new FormData(searchForm);
    const formObjectData = Object.fromEntries(formData);
    const searchParams = new URLSearchParams(formObjectData)

    const searchEndpoint = `${baseEndpoint}/search/?${searchParams}/`;
    
    const options = {
        method: "GET",
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('access')}`
        }
    };
    fetch(searchEndpoint, options).then(response => {
        return response.json();
    }).then(data => {
        const isValidData = !isNotValidToken(data);
        if (isValidData && contentContainer) {
            contentContainer.innerHTML = "";
            if (data & data.hits) {
                let htmlStr = '';
                for (let results of data.hits) {
                    htmlStr += `<li>${results.title}</li>`
                }
                contentContainer.innerHTML = htmlStr
            }
            else {
                contentContainer.innerHTML = `<p>No result Found</p>`
            }
        }
    }).catch(err => {
        console.log("err: ", err);
    })
}


function handleAuth(authData, callback) {
    localStorage.setItem('access', authData.access);
    localStorage.setItem('refresh', authData.refresh);

    if (callback) {
        callback();
    }
}


function getFetchOptions(method, body) {
    return {
        method: method ? method : "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`
        },
        body: body ? body : null
    }
}

function isNotValidToken(jsonData) {
    if (jsonData?.code === "token_not_valid") {
        // alert("Please login Again");
        return true;
    }
    return false
}

function refreshToken() {
    const endpoint = `${baseEndpoint}/api/token/refresh/`;
    
    const options = {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'refresh': localStorage.getItem('refresh')
        })
    };
    fetch(endpoint, options).then(response => {
        return response.json();
    }).then(x => {
        if (!isNotValidToken(x)) {
            localStorage.setItem('access', x.access);
            getProductList();
        }
        else {
            localStorage.clear('access')
            localStorage.clear('refresh')
            console.log('refresh: invalid');
        }
    }).catch(err => {
        console.log("err: ", err);    
    })
}


function validateToken() {
    const endpoint = `${baseEndpoint}/api/token/verify/`;
    
    const options = {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'token': localStorage.getItem('access')
        })
    };
    fetch(endpoint, options).then(response => {
        return response.json();
    }).then(x => {
        const isNotValid = isNotValidToken(x)
        if (isNotValid) {
            refreshToken();
        }
        else {
            console.log("validate: ", isNotValid)
            getProductList();
            
        }
    }).catch(err => {
        console.log("err: ", err);    
    })
}



function getProductList() {
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()

    fetch(endpoint, options)
        .then(response => response.json())
        .then(data => {
            const isNotValid = isNotValidToken(data)
            console.log("product: ", isNotValid)
            if (!isNotValid) {
                writeToContainer(data)
            }
        })
        .catch(err => {
            console.log("err: ", err);
        })
}

function writeToContainer(data) {
    if (contentContainer)
        contentContainer.innerHTML = `<pre>${JSON.stringify(data, null, 4)}</pre>`
}

validateToken();