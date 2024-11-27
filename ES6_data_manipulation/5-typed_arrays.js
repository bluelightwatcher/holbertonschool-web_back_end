export default function createInt8TypedArray(length, position, value) {
  // Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // Create a DataView to manipulate the buffer
  const view = new DataView(buffer);

  // Check if the position is within bounds
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Write the value at the specified position
  view.setInt8(position, value);

  return view;
}
