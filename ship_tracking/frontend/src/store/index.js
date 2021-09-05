import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        loadedVessel : [],
        currentPosition : [], 
    },
    mutations : {
        addVessel(state, vesselData) {
            state.loadedVessel = vesselData;
        },
        addCurrentPosition(state, vesselObject) {
            state.currentPosition = [vesselObject]
        }
    },
    getters: {
        allVesselPositions(state) {
            return state.loadedVessel
        }
    },
    actions: {

    },
    modules: {

    },
});
