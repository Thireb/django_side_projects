(async()=> {let permission = await Notification.requestPermission();})();

var allinfo = {
    names: document.getElementsByClassName("name"),
    phone_numbers: document.getElementsByClassName("phone_number"),
    amounts: document.getElementsByClassName("amount"),
    datecolls: document.getElementsByClassName("date")
};
const notify = elementid => {
    const title = "Debt Collection";
    const text = `Get ${allinfo.amounts[elementid].innerHTML} from ${allinfo.names[elementid].innerHTML}`    
    const notif = new Notification(`${title}`, {
        body: `${text}`,
    });
    setTimeout(() => { notif.close();}, 10*1000);
    notif.addEventListener('click', function(){
        alert(`Get ${allinfo.amounts[elementid].innerHTML} from ${allinfo.names[elementid].innerHTML}, Call ${allinfo.phone_numbers[elementid].innerHTML}`);
    });
    console.log(`${text}`);
};

const check_date = elementid => {
    const today = new Date();
    const debtdate = allinfo.datecolls[elementid].innerHTML;
    const date = debtdate.split("/");
    console.log("checking")
    if(date[0]==`${today.getDate()}` && date[1]==`${today.getMonth()+1}` && date[2]==`${today.getFullYear()}`) {
        notify(elementid);
    }
};

const refresh = () => {
    for (var i = 0; i < allinfo.names.length; i++){
        check_date(i)
    }
};
refresh()