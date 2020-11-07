paletteIDs = [];
inputColorIDs = [];

$('.palette').each(function () {
    paletteIDs.push(this.id);
    });

jQuery('.inputColor').each(function () {
    inputColorIDs.push(this.id)
});

function colorChange(){

    let valid = true;
    let hexList = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];

    for (let i=0; i<5; i++) {
        let temp = document.getElementById(inputColorIDs[i]).value.split('');
        if (temp.length !== 7) {
            valid = false
        } else if (temp[0] !== '#') {
            valid = false
        }
        for (let j = 1; j < 7; j++) {
            if (!(hexList.includes(temp[j]))) {
                valid = false
            }
        }

    }

    if (valid === true) {
        // console.log('wat')
        for (let k = 0; k < 5; k++) {
            document.getElementById(inputColorIDs[k]).placeholder = document.getElementById(inputColorIDs[k]).value;
            document.getElementById(inputColorIDs[k]).value = '';
            document.getElementById(paletteIDs[k]).style.backgroundColor =
                document.getElementById(inputColorIDs[k]).placeholder
        }
    } else {
        alert('Please enter a valid hex')
    }
}



