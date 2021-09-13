const domain = 'http://127.0.0.1:8000';

window.onload = function() {
    const username = document.querySelector('#id_username'),
          password = document.querySelector('#id_password'),
          authForm = document.querySelector('#auth_form');

    const authUpdater = new XMLHttpRequest();
    authUpdater.onreadystatechange = function() {
        if (authUpdater.readyState == 4) {
            if (authUpdater.status == 200) {
                data = JSON.parse(authUpdater.responseText);
                const newData = Object.entries(data)[1][1];
                console.log(newData);
                authForm.reset();
                return newData;
            } else {
                window.alert(authUpdater.statusText);
            }
        }
   
    }

    authForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const data = JSON.stringify({
            username: username.value,
            password: password.value
        });
        authUpdater.open('POST', domain + '/auth/jwt/create/', true);
        authUpdater.setRequestHeader('Content-Type', 'application/json');
        authUpdater.setRequestHeader('Accept', 'application/json');
        authUpdater.send(data);
    });

    
}