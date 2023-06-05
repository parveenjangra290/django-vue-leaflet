<template>
  <l-map
    :center="center"
    :zoom="zoom"
    class="map"
    ref="map"
    @update:zoom="zoomUpdated"
    @update:center="centerUpdated"
  >
    <l-tile-layer
    :url="url"/>
    <l-marker v-for="(farmer, index) in farmers"
    :key="index"
    ref="markersRef"
    :lat-lng="[farmer.latitude, farmer.longitude]"
    :icon="icon">
      <l-popup>
      <b>Name:</b> {{farmer.name}}<br>
      <b>Address:</b> {{farmer.village}}, {{farmer.block_tahsil}},
                {{farmer.district}}, {{farmer.state}}, {{farmer.country}}
      </l-popup>
    </l-marker>
  </l-map>
</template>

<script>
import Vue from 'vue'
import { LMap, LTileLayer, LMarker, LTooltip, LPopup, LControlZoom, LGeoJson, LFeatureGroup } from 'vue2-leaflet'
import { latLng, icon } from 'leaflet'
import 'leaflet/dist/leaflet.css'
Vue.component('l-marker', LMarker)
Vue.component('l-tooltip', LTooltip)
Vue.component('l-popup', LPopup)
Vue.component('l-control-zoom', LControlZoom)
Vue.component('l-geo-json', LGeoJson)
Vue.component('l-feature-group', LFeatureGroup)

export default {
  components: {
    LMap,
    LTileLayer
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      center: [ 23.4677934, 81.6978418 ],
      zoom: 5,
      farmers: [],
      icon: icon({
        iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
        iconSize: [32, 37],
        iconAnchor: [16, 37]
      })
    }
  },
  methods: {
    zoomUpdated (zoom) {
      this.zoom = zoom
      console.log(this.markers)
    },
    centerUpdated (center) {
      this.center = center
    },
    async getData () {
      try {
        // fetch tasks
        const response = await this.$http.get('http://127.0.0.1:8000/api/v1/farmers/')
        // console.log(response.data)
        this.farmers = response.data.farmers
      } catch (error) {
        // log the error
        console.log(error)
      }
    },
    farmerLocation (lat, long) {
      let l = latLng(lat, long)
      console.log(l)
      return l
    }
  },
  created: function () {
    this.getData()
  }
}
</script>

<style>
  .map {
    position: absolute;
    width: 100%;
    height: 100%;
    overflow :hidden
  }
</style>
