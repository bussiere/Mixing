An api to make comination of an array of string  :




import requests

# now we make the test
login_data = {
    "list": ["a", "b", "c","d"],
    "separator": ";",
}
r = requests.post("https://young-earth-75813.herokuapp.com/api/v1/combine", json=login_data)
print(r.status_code)
print(r.content)
b'{"result": ["a", "a;b", "a;b;c", "a;b;c;d", "a;b;d", "a;c", "a;c;d", "a;d", "b", "b;c", "b;c;d", "b;d", "c", "c;d", "d"]}'