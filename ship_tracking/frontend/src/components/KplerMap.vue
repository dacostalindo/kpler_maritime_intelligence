<template>
<div class="kpler">
    <l-map
        v-if="showMap"
        :zoom="zoom"
        :center="center"
        :options="mapOptions" 
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate"
    >
        <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
       <l-moving-marker
      v-for="l in locations"
      :key="l.id"
      :lat-lng="l.latlng"
      :duration=1000
      :keep-at-center="keepAtCenter"
      :icon="icon"
     >
      <l-popup :content="l.text" />
        </l-moving-marker>
    </l-map>
</div>
</template>

<script>

import L from 'leaflet';
import { latLng } from "leaflet";
import { LMap, LTileLayer} from 'vue2-leaflet';
import LMovingMarker from 'vue2-leaflet-movingmarker';



export default {
  name: 'MyAwesomeMap',
  components: {
    LMap,
    LTileLayer, 
    LMovingMarker,
  },
  data() {
      return {
            zoom: 13,
            center: latLng(47.41322, -1.219482),
            url: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
            attribution:
                '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            withPopup: latLng(47.41322, -1.219482),
            withTooltip: latLng(47.41422, -1.250482),
            currentZoom: 11.5,
            currentCenter: latLng(47.41322, -1.219482),
            showParagraph: false,
            mapOptions: {
                zoomSnap: 0.5
            },
            showMap: true,
            icon: L.icon({
                iconUrl:
                'https://s3-eu-west-1.amazonaws.com/ct-documents/emails/A-static.png',
                iconSize: [21, 31],
                iconAnchor: [10.5, 31],
                popupAnchor: [4, -25],
            })
        }
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
  }
};
</script>

<style>
.kpler{
    height: 500px; 
    width: 100%;
}


</style>