
fetch('https://amora-datapoint.herokuapp.com/', {
    method: 'GET',
    headers: {
        'Accept': 'application/json',
    },
})
.then(response => response.json())
.then(response => console.log(JSON.stringify(response)))