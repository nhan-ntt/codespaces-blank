import React, { useEffect } from "react";
import { playPause } from "../stores/player/currentAudioPlayer";
import { SongProps } from "../interfaces/Song";
import { useDispatch, useSelector } from "react-redux";
import { useState } from "react";
import { shadeColor } from "../configs/utils";
import { Image } from "@nextui-org/react";
import axios from "axios";

function HorizontalSongCard({
    song,
    onClick,
}: {
    song: SongProps;
    onClick: () => void;
}) {
    const [showPlayButton, setPlayButton] = useState(false);
    const { activeSong, isPlaying } = useSelector((state: any) => state.player);

    let songDemo = JSON.parse(JSON.stringify(song));
    songDemo.artist_name = "png";
    songDemo.artist_id = 1;
    songDemo.cover_image = {
        color: "black",
        url: "https://images3.alphacoders.com/690/690494.jpg",
    };

    return (
        <div
            key={songDemo.id}
            className="mr-4 cursor-grab"
            onClick={onClick}
            onMouseEnter={() => setPlayButton(true)}
            onMouseLeave={() => setPlayButton(false)}
        >
            <div
                className="p-4 bg-gradient-to-t from-[#2c2a2a4a] to-[#2c2a2ac7] hover:bg-[#4340409d]
           tablet:hover:bg-transparent mobile:hover:bg-transparent
           rounded h-full mini-laptop:p-3 tablet:p-0 tablet:from-transparent tablet:to-transparent
           mobile:from-transparent mobile:to-transparent mobile:p-0
           "
            >
                <div
                    className="
                    w-[200px] h-[200px] relative 
          mini-laptop:w-[140px] mini-laptop:h-[140px] 
          tablet:w-[130px] tablet:h-[130px] mobile:w-[100px] mobile:h-[100px]"
                >
                    {activeSong.id === songDemo.id ? (
                        <PlayPauseButton
                            condition={activeSong.id === songDemo.id}
                            isPlaying={isPlaying}
                        />
                    ) : showPlayButton ? (
                        <PlayPauseButton
                            condition={showPlayButton}
                            isHover
                            isPlaying={isPlaying}
                        />
                    ) : null}

                    <Image
                        src={songDemo.cover_image.url}
                        isZoomed
                        className="
                        z-6
                    w-[200px] h-[200px] relative 
          mini-laptop:w-[140px] mini-laptop:h-[140px] 
          tablet:w-[130px] tablet:h-[130px] rounded mobile:w-[100px] mobile:h-[100px] object-cover"
                    />
                </div>

                <p className="line-clamp-2 mt-3 text-base mobile:text-sm tablet:text-sm">
                    {songDemo.name}
                </p>
                <p
                    className="line-clamp-2 mt-0.5 text-sm text-gray-400 
            font-ProximaRegular mobile:text-xs tablet:text-xs"
                >
                    {songDemo.artist_name}
                </p>
            </div>
        </div>
    );
}

export function PlayPauseButton({
    condition,
    isPlaying,
    isHover,
}: {
    condition: boolean;
    isPlaying: boolean;
    isHover?: boolean;
}) {
    const dispatch = useDispatch();

    return (
        <div>
            {condition && (
                <div className="absolute w-full h-full bg-black bg-opacity-10 z-10 flex justify-end items-end rounded">
                    <div
                        onClick={() => dispatch(playPause(!isPlaying))}
                        className="mx-2 my-3 bg-[#2bb540] rounded-full cursor-pointer hover:scale-110
                     w-[45px] h-[45px] flex justify-center items-center mobile:w-[30px] mobile:h-[30px]"
                    >
                        {isHover ? (
                            <i className="icon-play text-[20px] ml-1 text-black mobile:text-[16px]" />
                        ) : !isPlaying ? (
                            <i className="icon-play text-[20px] ml-1 text-black mobile:text-[16px]" />
                        ) : (
                            <i className="icon-pause text-[20px] text-black mobile:text-[16px]" />
                        )}
                    </div>
                </div>
            )}
        </div>
    );
}

export default HorizontalSongCard;
