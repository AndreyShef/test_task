const domain = 'http://127.0.0.1:8000';

window.onload = function() {
    const id = document.querySelector('#id'),
          first_name = document.querySelector('#first_name'),
          last_name = document.querySelector('#last_name'),
          phone = document.querySelector('#phone');

    const contactLoader = new XMLHttpRequest();
    contactLoader.onreadystatechange = function() {
        if (contactLoader.readyState == 4) {
            if (contactLoader.status == 200) {
                const data = JSON.parse(contactLoader.responseText);
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
        e.prevent.Default();
        const url = e.target.href;
        contactLoader.open('GET', url, true);
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
        contactDeleter.send();
    }


    const list = document.querySelector('#list');
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
                for(let i = 0; i < links.length; i++) {
                    links[i].addEventListener('click', contactLoad);
                }
            }
        }
    }
    function contactsListLoad() {
        contactsListLoader.open('GET', domain + '/api/contacts/', true);
        contactsListLoader.send();
    }
    contactsListLoad();

    const contactUpdater = new XMLHttpRequest();
    contactUpdater.onreadystatechange = function() {
        if (contactUpdater == 4) {
            if ((contactUpdater == 200) || (contactUpdater ==201)) {
                contactLoad();
                contactForm.reset();
                id.value = '';
            } else {
                window.alert(contactUpdater.statusText);
            }
        }
    }

    const contactForm = document.querySelector('#contact_form');
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const vid = id.value;
        if (vid) {
            const url = '/api/contacts/' + vid + '/';
            const method = 'PUT';
        } else {
            const url = '/api/contacts/';
            const method = 'POST';
        }
        data = JSON.stringify({
            id: vid,
            first_name: first_name.value,
            last_name: last_name.value,
            phone: phone.value
        });
        contactUpdater.open(method, domain + url, true);
        contactUpdater.setRequestHeader('Content-Type', 'application/json');
        contactUpdater.send(data);
    });
}