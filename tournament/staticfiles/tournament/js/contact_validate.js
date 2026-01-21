function validateForm() {
  // Get form elements
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const subject = document.getElementById("subject").value;
  const mobile = document.getElementById("mobile").value;
  const message = document.getElementById("message").value;

  // Regular expressions for basic validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const mobileRegex = /^\d{10}$/; // Assuming 10-digit mobile number

  // Check if name is empty
  if (name === "") {
    alert("Please enter your name.");
    return false;
  }

  // Check if email is valid
  if (!emailRegex.test(email)) {
    alert("Please enter a valid email address.");
    return false;
  }

  // Check if subject is selected
  if (subject === "") {
    alert("Please select a subject.");
    return false;
  }

  // Check if mobile number is valid
  if (!mobileRegex.test(mobile)) {
    alert("Please enter a valid 10-digit mobile number.");
    return false;
  }

  // Check if message is empty
  if (message === "") {
    alert("Please enter a message.");
    return false;
  }

  // If all validations pass, return true
  return true;
}