function logout()
{alert('haha')}
function over(e)
{
	e.className='over'
}
function out(e)
{
	e.className='out'
}

function searchqq(e)
{
	arry=e.cells
	arry[5].innerHTML='<button style="background-color:red">已查看</button>'
	qqnum=arry[0].innerHTML
	url="/queryQQ?thenum="+qqnum
	window.open(url,"_blank")
}
function searchqun(e)
{
	arry=e.cells
	arry[5].innerHTML='<button style="background-color:red">已查看</button>'
	qunnum=arry[3].innerHTML
	url="/queryQun?thenum="+qunnum
	window.open(url,"_blank")
}
