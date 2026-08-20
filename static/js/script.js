function chooseImage(){

    document.getElementById("imageInput").click();

}

const imageInput=document.getElementById("imageInput");

const preview=document.getElementById("preview");

const removeBtn=document.getElementById("removeBtn");

const detectBtn=document.getElementById("detectBtn");

imageInput.addEventListener("change",function(){

    const file=this.files[0];

    if(file){

        preview.src=URL.createObjectURL(file);

        preview.style.display="block";

        removeBtn.style.display="inline-block";

        detectBtn.style.display="inline-block";

    }

});

function removeImage(){

    imageInput.value="";

    preview.src="";

    preview.style.display="none";

    removeBtn.style.display="none";

    detectBtn.style.display="none";

}