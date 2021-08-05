bool sample_texture(vec3 tex_curr_pos, inout vec4 curr_color, float tdelta,
                    float t, vec3 dir)
{
    vec3 tex_sample = textureOffset(ds_tex, tex_curr_pos, texture_offset).rgb;
    float map_sample = textureOffset(bitmap_tex, tex_curr_pos, texture_offset).r;
    if ((map_sample > 0.0) && (length(curr_color.rgb) < length(tex_sample))) {
        curr_color = vec4(tex_sample, 1.0);
    }
    return bool(map_sample > 0.0);
}

vec4 cleanup_phase(in vec4 curr_color, in vec3 dir, in float t0, in float t1) 
{
  return vec4(curr_color);
}
