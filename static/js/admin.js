
function over(e)
{
	e.className='over'
}
function out(e)
{
	e.className='out'
}

function autotype(e)
{	
	arry=e.cells
	document.getElementById('update').loginname.value=arry[1].innerHTML
	document.getElementById('update').passwd.value=arry[2].innerHTML
	document.getElementById('update').endtime.value=arry[3].innerHTML
	document.getElementById('update').contact.value=arry[6].innerHTML
}

