// the value should contains number
export function hasNumber(value) {
  return /\d/.test(value) ? true : false;
}

// the value should contains lowercase letters
export function hasLowerCaseLetter(value) {
  return /[a-z]/.test(value) ? true : false;
}

// the value should contains uppercase letters
export function hasUpperCaseLetter(value) {
  return /[A-Z]/.test(value) ? true : false;
}

// the value should contains special character
export function hasSpecialCharacter(value) {
  return /[\^\$*.[\]{}()!@#%&\/\\,<>':;|_~']/.test(value) ? true : false;
}
