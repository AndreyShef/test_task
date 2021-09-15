const domain = 'http://127.0.0.1:8000';

window.onload = function() {
    const username = document.querySelector('#id_username'),
          password = document.querySelector('#id_password'),
          pass = document.querySelector('#pass'),
          authForm = document.querySelector('#auth_form');

    // function goUrl() {document.location.href = `${domain}/contacts_list/`;}

    const authUpdater = new XMLHttpRequest();
          authUpdater.withCredentials = true;
          authUpdater.onreadystatechange = function() {
              if (authUpdater.readyState == 4) {
                  if (authUpdater.status == 200) {
                      data = JSON.parse(authUpdater.responseText);
                      const newData = Object.entries(data)[1][1];
                      localStorage.setItem('token', ''+ newData);
                      let authToken = localStorage.getItem('token');
                      authForm.reset();
                      pass.style.display = 'block'; 
                      return authToken;
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