let filter_active_btn = document.querySelector('.filter_slide_btn');
let filter_aside_block = document.querySelector('.filter_aside_block');
let filter_aside_X = document.querySelector('.filter_aside_X');

filter_active_btn.onclick = () => {
    if (filter_aside_block.classList.contains('active_filter_aside')) {
        filter_aside_block.classList.remove('active_filter_aside');
    } else {
        filter_aside_block.classList.add('active_filter_aside');
    }
};

filter_aside_X.onclick = () => {
    filter_aside_block.classList.remove('active_filter_aside');
}