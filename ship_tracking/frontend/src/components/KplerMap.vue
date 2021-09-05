<template>
  <div class="kpler">
    <!-- <button v-on:click="getLocation">Greet</button> -->
    <l-map :zoom="14" :center="initialLocation">
      <l-icon-default />
      <l-tile-layer :url="mapData.url" :attribution="mapData.attribution" />
      <l-moving-marker
        v-for="l in getLocations"
        :key="l.id"
        :lat-lng="l.latlng"
        :duration="duration"
        :keep-at-center="keepAtCenter"
        :icon="icon"
      >
        <l-popup :content="l.text" />
      </l-moving-marker>
    </l-map>
  </div>
</template>

<script>
import axios from "axios";
import L from "leaflet";
import { LMap, LTileLayer, LIconDefault, LPopup } from "vue2-leaflet";
import LMovingMarker from "vue2-leaflet-movingmarker";

function rand(n) {
  const max = n + 0.01;
  const min = n - 0.01;
  return Math.random() * (max - min) + min;
}

const locations = [];
for (let i = 0; i < 10; i++) {
  locations.push({
    id: i,
    latlng: L.latLng(rand(48.8929425), rand(2.3821873)),
    text: "Moving Marker #" + i,
  });
}

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
    duration: { type: Number, default: 2000 },
    keepAtCenter: { type: Boolean, default: false },
  },
  computed: {
    async getLocations() { 
      const vessel_id = this.$store.state.loadedVessel;
      const path = "http://localhost:5000/vessels/".concat(vessel_id);
      await this.getAPIlatLon(path)
      return 0 ;
    },
  },
  methods: {
    getAPIlatLon(path) {
      axios.get(path, { crossDomain: true }).then((res) => { 
        return res.data
      });
    }
  },
  data() {
    return {
      locations,
      icon,
      initialLocation: L.latLng(48.8929425, 2.3821873),
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
        if (value !== oldValue) {
          clearInterval(this.interval);
          const setRandomLatLng = () => {
            this.locations.forEach((location) => {
              location.latlng = L.latLng(rand(48.8929425), rand(2.3821873));
            });
          };
          this.interval = setInterval(() => {
            setRandomLatLng();
          }, value);
          setRandomLatLng();
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
