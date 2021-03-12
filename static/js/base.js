const formEl = document.querySelector('.form');
const responseEl = formEl.querySelector('.response');

formEl.addEventListener('submit', (e) => {
    e.preventDefault();
    const successRedirect = formEl.dataset.successRedirect;
    const method = formEl.dataset.method.toUpperCase();
    const body = (method === 'POST' || method === 'PUT') ? JSON.stringify(serializeForm(formEl)) : null

    fetch(formEl.action, {
        method: method,
        body: body
    })
        .then(r => {
            if(r.status === 200 && successRedirect) {
                window.location.href = successRedirect;
            } else {
                r.json()
                    .then(text => responseEl.textContent = extractResponseMsg(text))
            }
        });
});

const cpfField = formEl.querySelector('input[name=cpf]');
cpfField && new Cleave(cpfField, {
    blocks: [3, 3, 3, 2],
  delimiters: ['.', '.', '-'],
  numericOnly: true
});

const pisField = formEl.querySelector('input[name=pis]');
pisField && new Cleave(pisField, {
    blocks: [3, 5, 2, 1],
    delimiters: ['.', '.', '-'],
    numericOnly: true,
});


const deleteAccountEl = formEl?.querySelector('.deleteAccount');
deleteAccountEl?.addEventListener('click', (e) => {
    e.preventDefault();
    fetch('/api/users/me', {
        method: 'DELETE'
    }).then(r => {
        if (r.status === 200) {
            window.location.href = '/login'
        }
    })
});

const logoutEl = formEl?.querySelector('.logout');
logoutEl?.addEventListener('click', (e) => {
    e.preventDefault();
    fetch('/api/auth/logout', {
        method: 'GET'
    }).then(r => {
        if (r.status === 200) {
            window.location.href = '/login'
        }
    })
});


function extractResponseMsg(response) {
    let msg = response?.detail
    if(Array.isArray(msg)) {
        msg = msg[0]?.msg
    }
    return msg;
}

function serializeForm(form) {
    let formData = new FormData(form);
    let obj = {};
    formData.forEach((value, key) => {
          let keys = key.split('.');
          let last_key = keys.pop();

          keys.reduce(function(o, key) {
              return obj[key] = o[key] || {};
          }, obj)[last_key] = value;
    });
    return obj;
}