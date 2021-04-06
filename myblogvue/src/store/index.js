import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        currentIndex: -1,
        subBoxFlag: false,
        reply_name: '说点什么吧'
    },
    mutations: {
        showReply(state, payload) {
            if (state.subBoxFlag) {
                if (state.currentIndex === payload.index) {
                    const reply_name = '回复 @' + payload.reply_name + '：'
                    if (state.reply_name === reply_name) {
                        state.currentIndex = -1
                        state.subBoxFlag = false
                    }
                    else {
                        state.reply_name = payload.reply_name
                    }
                }
                else {
                    state.currentIndex = payload.index
                    state.subBoxFlag = false
                }
            }
            else {
                state.currentIndex = state.currentIndex === payload.index ? -1 : payload.index
                state.subBoxFlag = false
            }
            state.reply_name = '回复 @' + payload.reply_name + '：'
        },
        subClick(state, payload) {
            state.currentIndex = payload.parentIndex
            state.reply_name = '回复 @' + payload.reply_name + '：'
            state.subBoxFlag = true
        }
    }
})

export default store