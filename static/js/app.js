const usernameField = document.getElementById("username");
const submitButton = document.querySelector(".submit-btn");
const errorBox = document.getElementById("username_error");
const emailField = document.getElementById("email");
const emailBox = document.getElementById("email_error");

usernameField.addEventListener("keyup", (e) => {
  const usernameValue = e.target.value;

  //   make api call to server
  if (usernameValue.length > 0) {
    fetch("/valiadte_username/", { body: JSON.stringify({ username: usernameValue }), method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        if (data.username_error) {
          submitButton.setAttribute("disabled", "disabled");
          errorBox.innerHTML = `<p class=" text-xs text-red-600 mt-2" id="username-error">${data.username_error}</p>`;
        } else {
          errorBox.innerHTML = '<p class="hidden text-xs text-red-600 mt-2" id="username-error"></p>';
          submitButton.removeAttribute("disabled");
        }
      });
  }
});
emailField.addEventListener("keyup", (e) => {
  const emailValue = e.target.value;

  //   make api call to server
  if (emailValue.length > 0) {
    fetch("/valiadte_email/", { body: JSON.stringify({ email: emailValue }), method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        if (data.email_error) {
          submitButton.setAttribute("disabled", "disabled");
          emailBox.innerHTML = `<p class=" text-xs text-red-600 mt-2" id="username-error">${data.email_error}</p>`;
        } else {
          emailBox.innerHTML = '<p class="hidden text-xs text-red-600 mt-2" id="username-error">/p>';
          submitButton.removeAttribute("disabled");
        }
      });
  }
});
