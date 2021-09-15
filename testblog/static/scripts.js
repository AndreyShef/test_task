const domain = 'http://127.0.0.1:8000';

window.onload = function() {
    const id = document.querySelector('#id'),
          first_name = document.querySelector('#first_name'),
          last_name = document.querySelector('#last_name'),
          phone = document.querySelector('#phone');
    const contactForm = document.querySelector('#contact_form');
          

    const contactLoader = new XMLHttpRequest();
    contactLoader.onreadystatechange = function() {
        if (contactLoader.readyState == 4) {
            if (contactLoader.status == 200) {
                data = JSON.parse(contactLoader.responseText);
                id.value = data.id;
                first_name.value = data.first_name;
                last_name.value = data.last_name;
                phone.value = data.phone;

            } else {
                window.alert(contactLoader.statusText);
            }
        }
    }

    function contactLoad(e) {
        e.preventDefault();
        const url = e.target.href;
        contactLoader.open('GET', url, true);
        contactLoader.setRequestHeader('Authorization', 'Bearer ' + localStorage.getItem('token'));
        contactLoader.send();
    }

    const contactDeleter = new XMLHttpRequest();
    contactDeleter.onreadystatechange = function() {
        if (contactDeleter.readyState == 4) {
            if (contactDeleter.status == 204) {
                contactsListLoad();
            } else {
                window.alert(contactDeleter.statusText);
            }
        }
    }
    function contactDelete(e) {
        e.preventDefault();
        const url = e.target.href;
        contactDeleter.open('DELETE', url, true);
        contactDeleter.setRequestHeader('Authorization', 'Bearer ' + localStorage.getItem('token'));
        contactDeleter.send();
    }


    const contactsListLoader = new XMLHttpRequest();
    contactsListLoader.onreadystatechange = function() {
        if (contactsListLoader.readyState == 4) {
            if (contactsListLoader.status == 200) {
                const data = JSON.parse(contactsListLoader.responseText);
                let s = '<ul>';
                for (i = 0; i < data.length; i++) {
                    d = data[i];
                    detail_url = '<a href="' + domain + '/api/contacts/' + d.id + '/" class="detail">Вывести</a>';
                    delete_url = '<a href="' + domain + '/api/contacts/' + d.id + '/" class="delete">Удалить</a>';

                    s += '<li>' + d.first_name + ' ' + d.last_name + ' (' + d.phone + ') [' + detail_url + ' ' + delete_url + ']</li>';
                }
                s += '</ul>';
                list.innerHTML = s;
                links = list.querySelectorAll('ul li a.detail');
                for(i = 0; i < links.length; i++) {
                    links[i].addEventListener('click', contactLoad);
                }
                links = list.querySelectorAll('ul li a.delete');
                for(i = 0; i < links.length; i++) {
                    links[i].addEventListener('click', contactDelete);
                }
            } 
        }
    }
    function contactsListLoad() {
        contactsListLoader.open('GET', domain + '/api/contacts/', true);
        contactsListLoader.setRequestHeader('Authorization', 'Bearer ' + localStorage.getItem('token'));
        contactsListLoader.send();
    }
    contactsListLoad();

    const contactUpdater = new XMLHttpRequest();
    contactUpdater.onreadystatechange = function() {
        if (contactUpdater.readyState == 4) {
            if ((contactUpdater.status == 200) || (contactUpdater.status ==201)) {
                contactsListLoad();
                contactForm.reset();
                id.value = '';
            } else {
                window.alert(contactUpdater.statusText);
            }
        }
    }

    
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const vid = id.value;
        let   url = '',
              method = '';
        if (vid) {
            url = '/api/contacts/' + vid + '/';
            method = 'PUT';
        } else {
            url = '/api/contacts/';
            method = 'POST';
        }
        data = JSON.stringify({
            id: vid,
            first_name: first_name.value,
            last_name: last_name.value,
            phone: phone.value
        });
        contactUpdater.open(method, domain + url, true);
        contactUpdater.setRequestHeader('Content-Type', 'application/json');
        contactUpdater.setRequestHeader('Authorization', 'Bearer ' + localStorage.getItem('token'));
        contactUpdater.send(data);
    });
}