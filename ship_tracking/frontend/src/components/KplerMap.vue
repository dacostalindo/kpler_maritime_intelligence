<template>
  <div class="kpler">
    <l-map :zoom="4" :center="initialLocation">
      <l-icon-default />
      <l-tile-layer :url="mapData.url" :attribution="mapData.attribution" />
        <l-moving-marker
          v-for="l in location"
          :key="l.id"
          :lat-lng="l.latlng"
          :duration="duration"
          :keep-at-center="keepAtCenter"
          :icon="icon"
        >
        <l-popup />
      </l-moving-marker>
    </l-map>
  </div>
</template>

<script>

import L from "leaflet";
import { LMap, LTileLayer, LIconDefault, LPopup } from "vue2-leaflet";
import LMovingMarker from "vue2-leaflet-movingmarker";


const icon = L.icon({
  iconUrl:
    "https://s3-eu-west-1.amazonaws.com/ct-documents/emails/A-static.png",
  iconSize: [21, 31],
  iconAnchor: [10.5, 31],
  popupAnchor: [4, -25],
});

export default {
  name: "MyAwesomeMap",
  components: {
    LMap,
    LTileLayer,
    LMovingMarker,
    LIconDefault,
    LPopup,
  },
  props: {
    duration: { type: Number, default: 10},
    keepAtCenter: { type: Boolean, default: true },
  },
  computed: {
    location () {
        let currentPosition = this.$store.state.currentPosition;
        if (currentPosition.length) {
          return currentPosition
        }
        return {}
    },
  },
  data() {
      return {
        icon,
        initialLocation: L.latLng(22.519, 49.338),
        mapData: {
          attribution:
            '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
          url: "https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png",
        },
        interval: null,
      };
  },
  watch: {
    duration: {
      handler(value, oldValue) {
        let counter = 0 
        if (value !== oldValue) {
            clearInterval(this.interval)
            const setRandomLatLng = () => {
              let location = this.$store.getters.allVesselPositions
              if (location.length && counter < location.length) {
                this.$store.commit('addCurrentPosition', location[counter])
                counter = counter + 1
              }
            }
            this.interval = setInterval(() => {
              setRandomLatLng()
            }, value)
            setRandomLatLng()
        }
      },
      immediate: true,
    },
  },
};
</script>

<style>
.kpler {
  height: 100%;
  width: 100%;
}
</style>
