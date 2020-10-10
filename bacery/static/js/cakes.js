
const all_data = {

}


// document.onclick = function (e) {
//     if (e.target.classList.contains('checked-inputs')) {
//         var cake_features= new Array()
//         document.querySelectorAll('.checked-inputs').forEach(function (e) {
//                 if (e.checked == true) {
//                     var cake_feature = e.closest('.d-flex').querySelector('.choose-types').innerText
//                     cake_features.push(cake_feature)
                    
//                 }
//         })
//         all_data['cake_features'] = cake_features
//         loadAllData(all_data)

//     }
        

// }


document.onclick = function (e) {
    if (e.target.classList.contains('checked-inputs')) {
        
        var cake_types= new Array()
        var cake_features=new Array()
        document.querySelectorAll('.checked-inputs').forEach(function (e) {
            if (e.classList.contains('types')) {
                if (e.checked == true) {
                    var cake_type = e.closest('.d-flex').querySelector('.choose-types').innerText
                    cake_types.push(cake_type)
                    
                }
            }
            if (e.classList.contains('feature') && e.checked == true) {
                var cake_feature = e.closest('.d-flex').querySelector('.choose-types').innerText
                cake_features.push(cake_feature)
            }

        })
        all_data['cake_types'] = cake_types
        all_data['cake_features'] = cake_features
        loadAllData(all_data)

    }
}





document.querySelector('.min-price').addEventListener('input', (e) => {
    var minPrice = document.querySelector('.min-price').value
    all_data['minPrice'] = minPrice
    loadAllData(all_data)
})
document.querySelector('.max-price').addEventListener('input', (e) => {
    var maxPrice = document.querySelector('.max-price').value
    all_data['maxPrice'] = maxPrice
    loadAllData(all_data)
})

function loadAllData(data) {
    console.log(data)
    $.ajax({
        url: 'http://localhost:8000/api/v1.0/products/cakes/',
        method: "GET",
        data: data,
        success: function (response) {
            console.log(response)
            document.querySelector('.removed-data').innerHTML = ''
            console.log(response.page_range)
            for (cake of response.filtered_cakes) {
                document.querySelector('.removed-data').innerHTML +=`
                <div class="col-4 parent-of-card">
                        <div class="card">
                            <img src="${cake.main_image}" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">${cake.name}</h5>
                                <div class="d-flex justify-content-between w-100">
                                    <div>
                                        <span style="font-size: 14px;">Мин. заказ</span>
                                    </div>
                                    <div>
                                        <span style="font-size: 14px;">${cake.unit}</span>
                                        <span style="font-size: 14px;">${cake.name_of_unit}</span>
                                    </div>
                                </div>
                                <div class="d-flex justify-content-between w-100">
                                    <div>
                                        <span style="font-size: 14px;">Стоимость <small class="text-muted">(за мин. заказ)</small></span>
                                    </div>
                                    <div>
                                        <span>${cake.price}</span>

                                    </div>
                                </div>
                                <div class="py-2 mt-2">
                                    <a href="${cake.my_url}"
                                    class="btn btn-primary w-100 ">Открыть</a>
                                </div>
                            </div>
                        </div>
                    </div>`
                
            }
            document.querySelector('.old-pagi').innerHTML=''
            document.querySelector('.js-pagination').innerHTML=''
            for (var i =1;i<=response.page_range;i++){
                page_numbers=document.createElement('span')
                page_numbers.innerText=i
                page_numbers.href=`?page=${i}`
                document.querySelector('.js-pagination').appendChild(page_numbers)
                page_numbers.classList.add('m-2','pagination-numbers-js')

                page_numbers.addEventListener('click',function(){
                    all_data['page']=this.innerText
                    loadAllData(all_data)
                })
            }
            
        },
        error: function (error) {
            console.log(error)
        }
    })
}