import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        loadedVessel : []
    },
    mutations : {
        addVessel(state, vessel_id) {
            state.loadedVessel = [vessel_id];
        }
    },
    getters: {
        vesselToShow(state) {
            return state.loadedVessel;
        }
    },
    actions: {

    },
    modules: {

    },
});
