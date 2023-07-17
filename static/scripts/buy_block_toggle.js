let toggle = document.querySelector('.product_info_buy_block_fixed_toggle');
let block = document.querySelector('.product_info_buy_block');

toggle.onclick = () => {
    if (block.classList.contains('active_buy_block')) {
        block.classList.remove('active_buy_block');
    } else {
        block.classList.add('active_buy_block');
    }
};