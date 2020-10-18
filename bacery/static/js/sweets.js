
const all_data = {

}


document.onclick = function (e) {
    if (e.target.classList.contains('checked-inputs')) {
        var sweet_features= new Array()
        document.querySelectorAll('.checked-inputs').forEach(function (e) {
                if (e.checked == true) {
                    var sweet_feature = e.closest('.d-flex').querySelector('.choose-types').innerText
                    sweet_features.push(sweet_feature)
                    
                }
        })
        all_data['sweet_features'] = sweet_features
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
    console.log('heloooooooooooooooooooooooooooo')
    $.ajax({
        url: 'http://soffiabakery.ru/api/v1.0/products/sweets/',
        method: "GET",
        data: data,
        success: function (response) {
            console.log(response)
            document.querySelector('.removed-data').innerHTML = ''
            console.log(response.page_range)
            for (sweet of response.filtered_sweets) {
                document.querySelector('.removed-data').innerHTML +=`
                <div class="col-4 parent-of-card">
                        <div class="card">
                            <img src="${sweet.main_image}" class="card-img-top " alt="...">
                            <div class="card-body">
                                <h5 class="card-title">${sweet.name}</h5>
                                <p class="card-text">${sweet.short_description}</p>
                                <a href="${sweet.my_url}" class="btn btn-primary w-100">Открыть</a>
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
            console.log('error')
        }
    })
}