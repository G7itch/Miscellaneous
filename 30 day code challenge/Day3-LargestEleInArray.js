const message = 'Hello world' // Try edit me
const arr = []
var num = prompt(">> ")
var i = 0
while (num != "") {
  arr[i] = num
  var num = prompt(">> ")
  i+=1
}
// Log to console
var total = arr[0]
for (i = 0; i < arr.length; i++)
  if (arr[i] >= total)
    total = arr[i]

document.writeln(total)