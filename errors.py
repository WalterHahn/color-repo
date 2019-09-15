msgs = {
  1: "empty parameters",
  2: "missing parameters",
  3: "name greater than 32 characters",
  4: "hex length is not 6"
}


def result(code, status):
    return { "errors": msgs[code] }, status
