import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

export default createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "light",
    themes: {
      light: {
        colors: {
          primary: "#1976D2",
          secondary: "#FF4081",
        },
      },
      dark: {
        colors: {
          primary: "#90CAF9",
          secondary: "#F48FB1",
        },
      },
    },
  },
});
