module.exports = async function getSnakeRiverFlows() {
  const uri =
    "http://waterservices.usgs.gov/nwis/iv/?site=13022500&format=json";

  const xhr = new XMLHttpRequest();
  // YOLO!
  xhr.open("GET", uri);

  // Doesn't Work
  xhr.onload = () => {
    if (xhr.status === 200) {
      data = JSON.parse(xhr.responseText);
      console.log(data);
      return data;
    } else {
      console.log("Something went wrong!!");
    }
  };
};
