au BufRead,BufNewFile *.kv set syntax=kivy

let @k='zombiewalk.py'
set tags+=/Applications/Kivy.app/Contents/Resources/kivy/kivy/tags

"~/.vim/after/compiler/kivy.vim
let g:dispatch_compilers = {'kivy': 'kivy'}

nnoremap <F9> :update %<CR>:Dispatch kivy %<CR>
"nnoremap <F10> :update %<CR>:Dispatch kivy <C-R>k<CR>
nnoremap <F10> :update %<CR>:Start kivy <C-R>k<CR>
