package com.sa.web;

import com.sa.web.dto.SentenceDto;
import com.sa.web.dto.SentimentDto;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@CrossOrigin(origins = "*")
@RestController
public class SentimentController {

    @Value("${django_app.url}")
    private String djangoAppUrl;

    @PostMapping("/sentiment")
    public SentimentDto sentimentAnalysis(@RequestBody SentenceDto sentenceDto) {
        RestTemplate restTemplate = new RestTemplate();

        return restTemplate.getForObject(djangoAppUrl + "/api/analysis?sentence="+ sentenceDto.getSentence(), SentimentDto.class);
    }

    @GetMapping("/testHealth")
    public String testHealth() {
        return "Health Check";
    }
}